#!/usr/bin/env bash
# ==============================================================================
# Job B: Deployment Pipeline Script (Copy Artifact Consumer)
# Demonstrates retrieving build artifacts from Job A (build-job) and deploying
# ==============================================================================

set -euo pipefail

TARGET_ENV="${ENVIRONMENT:-staging}"
ARTIFACT_DIR="./copied_artifacts"

echo "=================================================================="
echo " Starting Job B: Deployment Pipeline Execution"
echo " Target Environment: ${TARGET_ENV}"
echo " Timestamp: $(date)"
echo "=================================================================="

# Verify artifact was copied from Job A by Copy Artifact plugin
if [ -d "${ARTIFACT_DIR}" ] && [ "$(ls -A "${ARTIFACT_DIR}")" ]; then
    echo "[SUCCESS] Found copied build artifact(s) from Job A:"
    ls -lh "${ARTIFACT_DIR}"
else
    echo "[INFO] Simulating direct artifact check in workspace:"
    mkdir -p "${ARTIFACT_DIR}"
    echo "Simulated copied jar artifact from Job A" > "${ARTIFACT_DIR}/sample-java-app-1.0.0.jar"
    ls -lh "${ARTIFACT_DIR}"
fi

echo "[DEPLOY] Deploying sample-java-app-1.0.0.jar to ${TARGET_ENV} server..."
sleep 1
echo "[SUCCESS] Application successfully deployed to ${TARGET_ENV}!"
echo "=================================================================="
