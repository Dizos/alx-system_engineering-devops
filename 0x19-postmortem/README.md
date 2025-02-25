#!/bin/bash
echo
'Postmortem: Troubles in API Gateway Outages with regards to latency Performance.

Issue Summary

Web access Platform noticed an outage from the 2-20-2025 for the period between 14:30 to 16:10 SAST. For,almost 60% of the clients of the platform, the response while authentication user, adding payment, or even retrieving content was sluggish. The level of traffic surged suddenly and was the main cause of the issue. This led to shortage in the connection pools from API gateway alongside control together with the backend services and services were worsened.

Timeline

14:30 SAST - Received notices through the monitoring application for higher level latency of API responses.

14:35 SAST - Engineers were not able to respond in time and started analyzing the problem, trying to locate the source of the problem and gafo as the most plausible suspect for the problem.

14:45 SAST - The initial examination of the database returned normal reports, which led to further examination of the API Gateway.

15:00 SAST - Connections made with backend services revealed there are abnormal amounts of connection failures.

15:15 SAST - Increases to the scale of the backend services were implemented by the engineers but the latency remained constant.

15:30 SAST - Networks team was assigned to the account to attempt scaling API Gateway to a higher level and account.

15:45 SAST - Increased traffic from one particular location ricocheted off other locations which resulted in AI Gateway’s close connection pool burst.

15:50 SAST - I applied an increase to the connection pool size and restarted the affected API Gateway instances.

16:05 SAST - There was a gradual improvement in latency and the affected services were back to normal.

16:10 SAST - Problem was fully resolved and the postmortem process was started.

Root Cause and Resolution

As the API Gateway reached the connection pool limit, it was unable to serve the backend services efficiently. The surge in traffic exhausted the connection thresholds that had been set and the result was timeouts and sluggish responses.

To fix the problem, I increased the connection pool size of the API Gateway and restarted the affected instances. This allowed the system to cope with the increased load and returned the performance to reasonable levels.

Corrective and Preventive Measures

To avoid similar incidents in the future, we intend to do the following:

Set the API Gateway connection pool limits to allow for future traffic surges.

Enable auto-scaling for the API Gateway so that the capacity can be raised or lowered based on demand.

Add additional connections to monitor the pool usage and set up alerts when they reach set thresholds.

Modify the incident response documentation to account for the configurations and provide effective and speedy response to enhance the ease of serving the API latency issues.

Carryout load testing to make sure our systems can serve during peak traffic waits to confirm that our infrastructure can support the peak levels.

Our goal is to enhance the system resilience and eliminate the chances of any future outages taking place by applying these measures.'
