import express, {Express} from 'express';
import dotenv from 'dotenv';
import {registerLoginEndPointFor} from "./login";
import {registerUserEndPointFor} from "./user";
import {registerJwkEndpointFor} from "./jwk";

dotenv.config();

const app: Express = express();
const port = process.env.PORT || "3000";

app.use(express.json());

registerLoginEndPointFor(app)
registerUserEndPointFor(app)
registerJwkEndpointFor(app)

app.listen(port, () => {
    console.log(`⚡️[server]: Server is running at https://localhost:${port}`);
});
