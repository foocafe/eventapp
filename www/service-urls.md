
# Service URLs

## REST things

To start with there is no support for `HEAD` and `OPTIONS` on any of the defined
resources, this might come later though.

## Resource(s) overview

*Table 1 Resources*
<table>
    <thead>
	<tr>
		<th>Resource</th>
		<th>Method(s)</th>
		<th>Description</th>
	</tr>
	</thead>
	<tbody>
    <tr>
        <td>Event</td>
        <td><code>GET, PUT, DELETE</code></td>
        <td>The one and only...</td>
    </tr>
    <tr>
        <td>Event registration controller</td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>Event collection</td>
        <td><code>GET, POST</code></td>
        <td>Collection of events. Supports query parameters</td>
    </tr>
    <tr>
        <td>Partner</td>
        <td><code>GET, PUT, DELETE</code></td>
        <td></td>
    </tr>
    <tr>
        <td>Partner collection</td>
        <td><code>GET, POST</code></td>
        <td>Collection of partners. </td>
    </tr>
	</tbody>
</table>


*Table 2 URIs*
<table>
    <thead>
    <tr>
        <th>Resource</th>
        <th>URI</th>
        <th>Descritpion</th>
    </tr>
    </thead>
    <tbody>
    <tr>
        <td>Event</td>
        <td><code>/api/v1/event</code></td>
        <td></td>
    </tr>
    <tr>
        <td>Event collection</td>
        <td><code>/api/v1/events?q={keyword}&tags={tag,tag2...}</code></td>
        <td></td>
    </tr>
    </tbody>
</table>

## Resource details

Tentative list of URIs for resources, stored, collection and controllers

    /api/v1/event

    /api/v1/event/<id>/venue/<id>
    /api/v1/event/<id>/venues


    /api/v1/event/<id>/register

    /api/v1/event/<id>/partner/<id>
    /api/v1/event/<id>/partners

    /api/v1/partner/<id>
    /api/v1/partners

### Event

Stores events

    /api/v1.0/event
    /api/v1/event/<event_id>

    GET

        Returns a specific event id.

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

    PUT
        /api/v1/events/731
        Update

    DELETE

        /api/v1/events/731
        Delete

### Event Collection

Collection of events, this collection is a read-only view of Event resources.

    /api/v1/events


### Ticket

    /api/v1.0/ticket
    /api/v1.0/ticket/<id>

### Partner

    /api/v1.0/partner
    /api/v1.0/partner/<id>