
# Service URLs

## Events

    /api/v1/events

    GET

        Returns all available future events.

        Order (?):

        Response (JSON):

            A list of event title and links, e.g.

            [
                {
                    "title": "The event",
                    "link": http://.../api/v1/events/731
                },
                {
                    "title": "The other event",
                    "link": http://.../api/v1/events/627
                },
                ...
            ]

    POST

        Create a new event

    PUT/DELETE

        Update or delete a specific event

