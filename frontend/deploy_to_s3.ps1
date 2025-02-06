# AWS S3 Deployment Script for Numbers API Frontend
# Run with: .\deploy_to_s3.ps1 -AwsProfile default -AwsRegion us-east-1

param(
    [string]$AwsProfile = "default",
    [string]$AwsRegion = "us-east-1"
)

# Logging functions
function Write-Info {
    param([string]$Message)
    Write-Host "[INFO] " -ForegroundColor Green -NoNewline
    Write-Host $Message
}

function Write-Warning {
    param([string]$Message)
    Write-Host "[WARNING] " -ForegroundColor Yellow -NoNewline
    Write-Host $Message
}

function Write-ErrorMessage {
    param([string]$Message)
    Write-Host "[ERROR] " -ForegroundColor Red -NoNewline
    Write-Host $Message
}

# Validate AWS CLI
function Test-AwsCli {
    try {
        $awsVersion = aws --version
        Write-Info "AWS CLI is installed: $awsVersion"
    }
    catch {
        Write-ErrorMessage "AWS CLI is not installed. Please install AWS CLI."
        exit 1
    }
}

# Create unique bucket name
$Timestamp = Get-Date -Format "yyyyMMddHHmmss"
$BucketName = "numbers-api-frontend-$Timestamp"

# Main deployment function
function Deploy-ToS3 {
    # Validate AWS CLI
    Test-AwsCli

    try {
        # Create S3 Bucket
        Write-Info "Creating S3 bucket: $BucketName"
        aws s3 mb "s3://$BucketName" --profile $AwsProfile --region $AwsRegion

        # Configure Static Website Hosting
        Write-Info "Configuring static website hosting"
        aws s3 website "s3://$BucketName/" `
            --index-document index.html `
            --error-document index.html `
            --profile $AwsProfile `
            --region $AwsRegion

        # Create temporary policy file
        $PolicyPath = [System.IO.Path]::GetTempFileName()
        $PolicyJson = @"
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "PublicReadGetObject",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::$BucketName/*"
        }
    ]
}
"@
        Set-Content -Path $PolicyPath -Value $PolicyJson

        # Set Public Read Access Policy
        Write-Info "Setting public read access policy"
        aws s3api put-bucket-policy `
            --bucket $BucketName `
            --policy file://$PolicyPath `
            --profile $AwsProfile `
            --region $AwsRegion

        # Create temporary CORS file
        $CorsPath = [System.IO.Path]::GetTempFileName()
        $CorsJson = @"
{
    "CORSRules": [
        {
            "AllowedHeaders": ["*"],
            "AllowedMethods": ["GET", "HEAD"],
            "AllowedOrigins": ["*"],
            "ExposeHeaders": []
        }
    ]
}
"@
        Set-Content -Path $CorsPath -Value $CorsJson

        # Configure CORS
        Write-Info "Configuring CORS"
        aws s3api put-bucket-cors `
            --bucket $BucketName `
            --cors-configuration file://$CorsPath `
            --profile $AwsProfile `
            --region $AwsRegion

        # Upload Files
        Write-Info "Uploading files to S3"
        aws s3 sync . "s3://$BucketName/" `
            --exclude ".git/*" `
            --exclude "deploy_to_s3.ps1" `
            --exclude "README.md" `
            --acl public-read `
            --profile $AwsProfile `
            --region $AwsRegion

        # Print Website URL
        $WebsiteEndpoint = "http://$BucketName.s3-website-$AwsRegion.amazonaws.com"
        Write-Info "🌐 Website deployed successfully!"
        Write-Host "Website URL: " -ForegroundColor Green -NoNewline
        Write-Host $WebsiteEndpoint -ForegroundColor Cyan
        Write-Warning "Note: It may take a few minutes for the website to be fully accessible."

        # Clean up temporary files
        Remove-Item $PolicyPath, $CorsPath -ErrorAction SilentlyContinue
    }
    catch {
        Write-ErrorMessage "Deployment failed: $_"
    }
}

# Run deployment
Deploy-ToS3
