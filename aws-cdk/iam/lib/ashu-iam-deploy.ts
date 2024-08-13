import * as cdk from 'aws-cdk-lib';
import { Construct } from 'constructs';
import * as iam from 'aws-cdk-lib/aws-iam';

// import * as sqs from 'aws-cdk-lib/aws-sqs';

export class IamStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);
    // Create an IAM group
    const group = new iam.Group(this, 'MyGroup', {
      groupName: 'MyGroup', // Specify the name of your IAM group
    });

    // Attach the AdministratorAccess policy to the group by name 
    group.addManagedPolicy(iam.ManagedPolicy.fromAwsManagedPolicyName('AdministratorAccess'));
     
    // Attach the AdministratorAccess policy to the group using its ARN
    const adminAccessPolicyArn = 'arn:aws:iam::aws:policy/AmazonS3FullAccess';
    group.addManagedPolicy(iam.ManagedPolicy.fromManagedPolicyArn(this, 'AdminAccessPolicy', adminAccessPolicyArn));

    // Create an IAM role
    const role = new iam.Role(this, 'MyRole', {
      assumedBy: new iam.ServicePrincipal('ec2.amazonaws.com'), // Example principal
      roleName: 'ashuMyRole',
    });

    // Attach a policy to the role
    const policyArn = 'arn:aws:iam::aws:policy/AdministratorAccess'; // Example policy ARN
    role.addManagedPolicy(iam.ManagedPolicy.fromManagedPolicyArn(this, 'AdminAccessPolicy1', policyArn));
    // Create a custom policy
    const customPolicy = new iam.Policy(this, 'CustomPolicy', {
      policyName: 'MyCustomPolicy',
      statements: [
        new iam.PolicyStatement({
          actions: ['s3:ListBucket'], // Example action
          resources: ['arn:aws:s3:::my-bucket'], // Example resource
        }),
      ],
    });

    // Attach the custom policy to the role
    role.attachInlinePolicy(customPolicy);

    // SPEC PART 
    // Add a trust policy to allow the IAM user to assume the role
    // role.addToPolicy(new iam.PolicyStatement({
    //   actions: ['sts:AssumeRole'],
    //   resources: [role.roleArn],
    //   principals: [new iam.ArnPrincipal('arn:aws:iam::992382386705:user/surbhi')] // Replace with the user's ARN
    // }));

    // Create a policy that allows the user to assume the role
    const assumeRolePolicy = new iam.Policy(this, 'AssumeRolePolicy', {
      policyName: 'AllowAssumeRolePolicy',
      statements: [
        new iam.PolicyStatement({
          actions: ['sts:AssumeRole'],
          resources: [role.roleArn],
        }),
      ],
    });

    // Attach the policy to the user
    const user1 = iam.User.fromUserName(this, 'ExistingUser1', 'surbhi'); // Replace with the actual user name
    user1.attachInlinePolicy(assumeRolePolicy);
    // SPEC PART END 
    // Add an existing user to the group
    // Note: Replace `surbhi` with the actual user name and ensure that the user exists
    const user = iam.User.fromUserName(this, 'ExistingUser', 'surbhi');

    // Add the user to the group
    group.addUser(user);
    // Create a new IAM user called 'delashu'
    const newUser = new iam.User(this, 'NewUser', {
      userName: 'delashu',
    });

    // Add the new user to the existing group
    group.addUser(newUser);

  }

}
