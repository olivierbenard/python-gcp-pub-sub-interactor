"""
Module holding the subscriber logic.
"""

import os
from typing import Any
from google.cloud import pubsub_v1
from python_gcp_pub_sub_interactor.constants import ENCODING
from python_gcp_pub_sub_interactor import settings


os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = settings.GOOGLE_SERVICE_ACCOUNT_KEYFILE


def callback(message: pubsub_v1.subscriber.message.Message) -> Any:
    """
    Method printing the given message in the terminal.
    """
    print(f"Received message: {message.data.decode(ENCODING)}")
    message.ack()


class SubscriberClient:  # pylint: disable=too-few-public-methods
    """
    Client for the GCP Subscriber.
    """

    def __init__(self, project: str, subscription: str) -> None:
        self.project = project
        self.subscription = subscription
        self.client = pubsub_v1.SubscriberClient()
        self.subscription_path = self.client.subscription_path(
            project=project, subscription=subscription
        )

    def start_subscriber(self) -> None:
        """
        Method starting an infinite loop, listening to the incoming messages
        in the gcp subscription.
        """
        streaming_pull_future = self.client.subscribe(
            self.subscription_path, callback=callback
        )
        print(f"Listening for messages on {self.subscription_path}...")
        try:
            streaming_pull_future.result()
        except KeyboardInterrupt:
            streaming_pull_future.cancel()
            print("Subscriber interrupted by user, shutting down.")


def main() -> None:
    """
    Main method to unstack and read messages from the subscriber.
    """
    subscriber_client = SubscriberClient(
        project=settings.GOOGLE_PROJECT_ID, subscription=settings.GOOGLE_SUBSCRIPTION_ID
    )
    subscriber_client.start_subscriber()


if __name__ == "__main__":
    main()
