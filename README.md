robotdyl
========

FLE's build server, running at [Insert Production URL here].

The app is designed as a set of microservices that communicate through
a task queue. The components right now are:

1. An API that receives notifications from GitHub*
1. A service for stripping out unnecessary files common in all supported platforms*
1. A service for compiling for all supported platforms (Windows, OS X and Linux)*
1. A frontend for manually triggering a build*
1. A frontend for build and install stats*


(* Not implemented yet)
