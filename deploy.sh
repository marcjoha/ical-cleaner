#!/bin/bash

# Deploy to Google Cloud Run
gcloud run deploy ical-cleaner --project REPLACE --platform managed --source . --region REPLACE --allow-unauthenticated
