import * as cdk from 'aws-cdk-lib';
import { Construct } from 'constructs';
// import * as sqs from 'aws-cdk-lib/aws-sqs';
import * as lambda from 'aws-cdk-lib/aws-lambda';
import * as path from 'path';
//import * as iam from 'aws-cdk-lib/aws-iam';
import * as events from 'aws-cdk-lib/aws-events';
import * as targets from 'aws-cdk-lib/aws-events-targets';
import * as s3 from 'aws-cdk-lib/aws-s3';
import * as s3Notifications from 'aws-cdk-lib/aws-s3-notifications';
//import * as lambdaEventSources from 'aws-cdk-lib/aws-lambda-event-sources';



export class AwsAshuLambdaStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // The code that defines your stack goes here
    // Use an existing IAM role by ARN
    // const existingRoleArn = 'arn:aws:iam::992382386705:role/service-role/ashu-py-function-role-az2r2nx4';
    // const existingRole = iam.Role.fromRoleArn(this, 'ExistingRole', existingRoleArn);

    // Define the Lambda function 
    // this will automatically create a new Role 
    const lambdaFunction = new lambda.Function(this, 'HelloAshu007Function', {
      functionName: 'helloashu0078989',
      runtime: lambda.Runtime.PYTHON_3_10, // Specify Python runtime
      handler: 'lambda_function.lambda_handler', // 'lambda_function' is the filename, 'lambda_handler' is the function name
      code: lambda.Code.fromAsset(path.join(__dirname, '../lambda/helloashu007')), // Path to the Lambda function code
      
    });
    // Create a CloudWatch Events rule to trigger the Lambda function
    // new events.Rule(this, 'HelloAshuEvent', {
    //   ruleName: 'helloashuevent',
    //   schedule: events.Schedule.rate(cdk.Duration.minutes(5)), // Run every 5 minutes
    //   targets: [new targets.LambdaFunction(lambdaFunction)],
    // });

    // Create an S3 bucket
    const bucket = new s3.Bucket(this, 'AshutoshBucket', {
      bucketName: 'ashutoshh007788-cdk0088', // Specify the name of your S3 bucket
      removalPolicy: cdk.RemovalPolicy.DESTROY, // Remove bucket on stack deletion (use cautiously)
    });

    // Add an event source to the Lambda function to trigger on S3 object creation events
    // lambdaFunction.addEventSource(new lambdaEventSources.S3EventSource(bucket, {
    //   events: [s3.EventType.OBJECT_CREATED], // Trigger Lambda on object creation
    // }));
    // Add an event notification to the S3 bucket for object creation events
    bucket.addEventNotification(s3.EventType.OBJECT_CREATED, new s3Notifications.LambdaDestination(lambdaFunction));

  }
}
