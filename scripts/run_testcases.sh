#!/usr/bin/env bash
# Note: when first run this script or migrations are updated, please remove the options --nomigrations and --reuse-db

# py.test --disable-socket --nomigrations -W error::RuntimeWarning --reuse-db --cov=src --cov-report html:test_cov_report tests/ #running with new migrations


py.test --disable-socket -W error::RuntimeWarning --cov=src --cov-report html:test_cov_report tests/ #running without new migrations
