"""
Module holding the publisher logic.
"""

import os
from google.cloud import pubsub_v1
from python_gcp_pub_sub_interactor.constants import ENCODING
from python_gcp_pub_sub_interactor import settings


os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = settings.GOOGLE_SERVICE_ACCOUNT_KEYFILE


class PublisherClient:  # pylint: disable=too-few-public-methods
    """
    Client for the GCP Publisher.
    """

    def __init__(self, project: str, topic: str) -> None:
        self.project = project
        self.topic = topic
        self.client = pubsub_v1.PublisherClient()
        self.topic_path = self.client.topic_path(project=project, topic=topic)

    def publish_message(self, message: str) -> None:
        """
        Method publishing the giving message in
        the publisher queue.
        """
        future = self.client.publish(
            topic=self.topic_path, data=message.encode(ENCODING)
        )
        print(f"Message published. Message ID: {future.result()}")


def main() -> None:
    """
    Main method to publish the messages into the stack.
    """

    publisher_client = PublisherClient(
        project=settings.GOOGLE_PROJECT_ID, topic=settings.GOOGLE_TOPIC_ID
    )

    try:
        while True:
            message = str(input("Message to publish: "))
            publisher_client.publish_message(message=message)
    except KeyboardInterrupt:
        print("Publisher interrupted by user, shutting down.")


if __name__ == "__main__":
    main()
