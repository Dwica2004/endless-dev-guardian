# Endless Dev Guardian

Endless Dev Guardian is a lightweight proof-of-concept static analysis tool designed to help developers identify common logic risks in Move-based smart contracts within the Endless ecosystem.

## Background
As the Endless ecosystem grows, more developers—especially new contributors—are building Move smart contracts. However, subtle logic vulnerabilities such as replay risks, weak access control, and unsafe execution order are often difficult to detect early.

## Problem
Currently, there is no simple, beginner-friendly security assistant tailored specifically for Endless Move contracts that helps developers detect common logic risks before deployment.

## Solution
Endless Dev Guardian provides a lightweight rule-based static scan for Move smart contracts. It highlights potential high-risk patterns and helps developers quickly identify issues related to security and contract logic.

## Features
- Detects replay / double execution patterns
- Identifies weak access control usage
- Flags event emission before final state update
- Simple CLI-based interface
- Easily extendable rule system

## Project Structure
