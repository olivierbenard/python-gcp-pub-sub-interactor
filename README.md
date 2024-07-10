# python-gcp-pub-sub-interactor

A small python project to publish and subscribe to a GCP Pub/Sub topic.

## Prerequisites

1. Install and configure [Google Cloud SDK](https://cloud.google.com/sdk/docs/install-sdk)
2. On [Google Cloud Console](https://console.cloud.google.com/), create a Pub/Sub topic
3. On [Google Cloud Console](https://console.cloud.google.com/), create a Pub/Sub subscription for that topic
4. Create a [Service Account](https://console.cloud.google.com/iam-admin/serviceaccounts) with *Pub/Sub Publisher* and *Pub/Sub Subscriber* rights.

**Note:** at the time of this writing, creating a topic automatically creates a subscription for that topic.

## Usage

First, edit the `settings.toml` configurations:

```toml
[default]
GOOGLE_PROJECT_ID = "your-project-id"
GOOGLE_TOPIC_ID = "your-topic-id"
GOOGLE_SUBSCRIPTION_ID = "your-subscription-id"
GOOGLE_SERVICE_ACCOUNT_KEYFILE = "path/to/your/service-account-file.json"
```

Then, download the json keyfile for the service account under the `secrets/` folder.

Finally:

* To publish messages to the Pub/Sub topic publisher:

        zsh> make publish
        Message to publish:

* To start the listening loop to subscribe and receive messages from the Pub/Sub subscription:

        zsh> make subscribe
        Listening for messages on projects/project_id/subscriptions/subscription_id...
