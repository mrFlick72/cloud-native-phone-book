import express, {Express} from 'express';
import dotenv from 'dotenv';
import {registerLoginEndPointFor} from "./login";
import {registerUserEndPointFor} from "./user";
import {registerJwkEndpointFor} from "./jwk";
import {registerHealthEndPointFor} from "./health";

dotenv.config();

const app: Express = express();
let port = Number(process.env.APPLICATION_PORT) || 3000;

const actuatorApp: Express = express();
const actuatorPort = port + 1

app.use(express.json());

registerLoginEndPointFor(app)
registerUserEndPointFor(app)
registerJwkEndpointFor(app)

registerHealthEndPointFor(actuatorApp)

app.listen(port, () => {
    console.log(`⚡️[server]: Server is running at http://localhost:${port}`);
});

actuatorApp.listen(actuatorPort, () => {
    console.log(`⚡️[server]: Server is running at http://localhost:${actuatorPort}`);
});
