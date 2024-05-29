import * as cdk from 'aws-cdk-lib';
import { Construct } from 'constructs';
import * as ecr from 'aws-cdk-lib/aws-ecr'
// import * as sqs from 'aws-cdk-lib/aws-sqs';

export class EcrStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // creating ECR 
   const ashurepo = new ecr.Repository(this,'ashu-repo',{
    repositoryName: 'ashucustom-repocdk',
    removalPolicy: cdk.RemovalPolicy.DESTROY,
    imageTagMutability: ecr.TagMutability.IMMUTABLE,
    imageScanOnPush: true
   });
  }
}
