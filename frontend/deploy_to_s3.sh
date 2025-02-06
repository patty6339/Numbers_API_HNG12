#!/bin/bash

# S3 Deployment Script for Numbers API Frontend
# Usage: ./deploy_to_s3.sh <aws_profile> <region>

# Exit on any error
set -e

# Check for required arguments
if [ $# -lt 2 ]; then
    echo "Usage: $0 <aws_profile> <region>"
    echo "Example: $0 default us-east-1"
    exit 1
fi

# Input parameters
AWS_PROFILE=$1
AWS_REGION=$2

# Generate unique bucket name
TIMESTAMP=$(date +"%Y%m%d%H%M%S")
BUCKET_NAME="numbers-api-frontend-${TIMESTAMP}"

# Color codes for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Logging functions
log_info() {
    echo -e "${GREEN}[INFO]${NC} $1"
}

log_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

log_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Validate AWS CLI installation
validate_aws_cli() {
    if ! command -v aws &> /dev/null; then
        log_error "AWS CLI is not installed. Please install it first."
        exit 1
    fi
}

# Check AWS credentials
validate_aws_credentials() {
    log_info "Validating AWS credentials..."
    if ! aws sts get-caller-identity --profile "$AWS_PROFILE" &> /dev/null; then
        log_error "Invalid AWS credentials. Please configure using 'aws configure --profile $AWS_PROFILE'"
        exit 1
    fi
}

# Create S3 Bucket
create_s3_bucket() {
    log_info "Creating S3 bucket: ${BUCKET_NAME}"
    aws s3 mb "s3://${BUCKET_NAME}" --profile "$AWS_PROFILE" --region "$AWS_REGION"
}

# Configure S3 for static website hosting
configure_static_website() {
    log_info "Configuring static website hosting"
    aws s3 website "s3://${BUCKET_NAME}/" \
        --index-document index.html \
        --error-document index.html \
        --profile "$AWS_PROFILE" \
        --region "$AWS_REGION"
}

# Set public read access policy
set_bucket_policy() {
    log_info "Setting public read access policy"
    aws s3api put-bucket-policy \
        --bucket "$BUCKET_NAME" \
        --policy "{
            \"Version\": \"2012-10-17\",
            \"Statement\": [
                {
                    \"Sid\": \"PublicReadGetObject\",
                    \"Effect\": \"Allow\",
                    \"Principal\": \"*\",
                    \"Action\": \"s3:GetObject\",
                    \"Resource\": \"arn:aws:s3:::${BUCKET_NAME}/*\"
                }
            ]
        }" \
        --profile "$AWS_PROFILE" \
        --region "$AWS_REGION"
}

# Configure CORS
configure_cors() {
    log_info "Configuring CORS"
    aws s3api put-bucket-cors \
        --bucket "$BUCKET_NAME" \
        --cors-configuration "{
            \"CORSRules\": [
                {
                    \"AllowedHeaders\": [\"*\"],
                    \"AllowedMethods\": [\"GET\", \"HEAD\"],
                    \"AllowedOrigins\": [\"*\"],
                    \"ExposeHeaders\": []
                }
            ]
        }" \
        --profile "$AWS_PROFILE" \
        --region "$AWS_REGION"
}

# Upload files to S3
upload_files() {
    log_info "Uploading files to S3"
    aws s3 sync . "s3://${BUCKET_NAME}/" \
        --exclude ".git/*" \
        --exclude "deploy_to_s3.sh" \
        --exclude "README.md" \
        --acl public-read \
        --profile "$AWS_PROFILE" \
        --region "$AWS_REGION"
}

# Print website endpoint
print_website_url() {
    WEBSITE_ENDPOINT="http://${BUCKET_NAME}.s3-website-${AWS_REGION}.amazonaws.com"
    log_info "🌐 Website deployed successfully!"
    echo -e "${GREEN}Website URL:${NC} ${WEBSITE_ENDPOINT}"
    echo -e "${YELLOW}Note: It may take a few minutes for the website to be fully accessible.${NC}"
}

# Main deployment function
main() {
    validate_aws_cli
    validate_aws_credentials
    create_s3_bucket
    configure_static_website
    set_bucket_policy
    configure_cors
    upload_files
    print_website_url
}

# Run the deployment
main

exit 0
