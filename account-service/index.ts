import express, {Express, Request, Response} from 'express';
import dotenv from 'dotenv';
import {registerLoginEndPointFor} from "./login";
import {registerUserEndPointFor} from "./user";

dotenv.config();

const app: Express = express();
const port = process.env.PORT || "3000";

app.use(express.json());

registerLoginEndPointFor(app)
registerUserEndPointFor(app)

app.listen(port, () => {
    console.log(`⚡️[server]: Server is running at https://localhost:${port}`);
});
