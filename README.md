![logo_glow.png](static%2Flogo_glow.png)

This is a simple backend for the `SustainabLLM` web application. It uses Flask for serving requests and nginx as a reverse proxy. 
Everything can be run through `docker-compose run`. 

The only currently supported functionality is asking a question and receiving answer aggregated from different sources as well as a list of those sources.