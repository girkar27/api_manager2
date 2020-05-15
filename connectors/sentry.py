import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration

sentry_sdk.init('root@localhost',integrations=[FlaskIntegration()])