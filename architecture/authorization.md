## How would you design the authorization of microservices?

Goals: authorize quickly and ease of management.

Use an ACL microservice which centralizes all authorization info. It
may use any document oriented database (dynamodb for instance). Each
microservice consults this system to decide if an action is
allowed. This information must be cached at client side with a
periodic refresh rate but there must be a specific endpoint for
immediate cache invalidation (listening to a topic to know when to
invalidate would be nice).
