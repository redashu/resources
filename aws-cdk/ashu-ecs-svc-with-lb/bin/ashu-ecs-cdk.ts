#!/usr/bin/env node
import 'source-map-support/register';
import * as cdk from 'aws-cdk-lib';
import { AshuEcsCdkStack } from '../lib/ashu-ecs-cdk-stack';

const app = new cdk.App();
new AshuEcsCdkStack(app, 'AshuEcsCdkStack', {
  // aws account id and region code name 
  env: { account: '751136288263', region: 'us-east-1' }

  /* For more information, see https://docs.aws.amazon.com/cdk/latest/guide/environments.html */
});