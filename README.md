## Debian/Ubuntu Package Visualizer

This is a demo application built with FastAPI and SvelteKit+TailwindCSS as part of a 6 hour hackathon.

Running the backend on a linux host will expose a package API that provides the following:
- /all : Returns a list of all packages
- /package/<name> : Returns details of a single package

In the package details, you can find things like dependencies + constraints, as well as reverse dependencies and alternatives.

![image](https://user-images.githubusercontent.com/8523191/187025673-3ee44f46-0e6c-4f58-9931-80160c0e67fa.png)

For packages introduced as the backend is running, they will not be shown as the packages are analyzed only once on backend startup.
A dependency graph is built on startup and stored in memory for simplicity.

## How to run the app

```bash
cd linux-package-visualizer
docker-compose up
```

And then visit http://localhost:3000

You can also run the backend and frontend separately. The frontend requires an 'API_URL' environment variable when building, and this is how it knows to find the backend.

