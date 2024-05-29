import * as cdk from 'aws-cdk-lib';
import { Construct } from 'constructs';
import * as ec2 from 'aws-cdk-lib/aws-ec2'
import * as ecs from  'aws-cdk-lib/aws-ecs'
import * as elbv2 from 'aws-cdk-lib/aws-elasticloadbalancingv2'
// import * as sqs from 'aws-cdk-lib/aws-sqs';

export class AshuEcsCdkStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);
    // refering to existing vpc 
    const vpc = ec2.Vpc.fromLookup(this,'ashuExistingVpc', {
      vpcId: 'vpc-0613e72a46c8cb335'
    });
    // defining ECS cluster info 
    const cluster = new ecs.Cluster(this,'ashu-ecs-cluster',{
      clusterName: 'ashu-ecs-bycdk',
      vpc: vpc,
      enableFargateCapacityProviders: true ,
      containerInsights: true // enable cloudwatch monitoring 
    });
    // add ec2 capacity 
    cluster.addCapacity('defaultashuScaleGroup',{
      instanceType: new ec2.InstanceType("t2.small"),
      desiredCapacity: 0, // container instances
      minCapacity: 0,
      maxCapacity: 5
    });

    // task Definition of farget launch type 
    const ashuTaskDef = new ecs.FargateTaskDefinition(this,'ashu-frg-task1',{
      cpu:  256,
      memoryLimitMiB: 512
       
    });
    // adding container info 
    const container = ashuTaskDef.addContainer('ashucdkc1',{
      image: ecs.ContainerImage.fromRegistry('docker.io/dockerashu/ashu-customer:bmoappv1'),
      memoryLimitMiB: 256,
      portMappings: [{ containerPort: 80 }]
    });
    // creating security group 
    const ashusecgroup = new ec2.SecurityGroup(this,'ashufirewallgrp',{
      vpc: vpc,
      description: 'allow ingress rules for 80 port'
    });
    ashusecgroup.addIngressRule(ec2.Peer.anyIpv4(),ec2.Port.tcp(80),'allow http traffic');
    // creating service using above task defintion 

    // Creating ALB 
    const ashulb = new elbv2.ApplicationLoadBalancer(this,'ashualbcdk',{
      vpc: vpc,
      internetFacing: true
    });
    // creating listener 
    const ashuListern = ashulb.addListener('ashunodelistner',{
       port: 80,
       open: true
    });
    const service = new ecs.FargateService(this,'ashuECSserviceCDK',{
      cluster,
      taskDefinition: ashuTaskDef,
      serviceName: 'ashu-svc-bycdk',
      desiredCount: 1,
      assignPublicIp: true,
      securityGroups: [ashusecgroup]   // attaching security group 
    });

    // attaching alb to service 
   ashuListern.addTargets('ashuvms',{
    port: 80,
    targets: [service.loadBalancerTarget({
      containerName: 'ashucdkc1',
      containerPort: 80
    })],
    healthCheck: {
      interval: cdk.Duration.seconds(60),
      path: "/",
      timeout: cdk.Duration.seconds(5)
    }
   });
   
  }
}
