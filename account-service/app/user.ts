import pg from 'pg';
import {Express, Request, Response} from "express";


const {Pool} = pg

const pool = new Pool({
    user: 'postgres',
    password: 'postgres',
    host: 'localhost',
    port: 5436,
    database: 'postgres',
})


export type User = {
    userName: string
    password: string,
    firstName: string,
    lastName: string,
}

export interface UserRepository {

    findUserBy(userName: string): Promise<User>

    save(user: User): Promise<void>

}

export function userRepository() {
    return new PostGressUserRepository()
}

class PostGressUserRepository implements UserRepository {
    async findUserBy(userName: string): Promise<User> {
        const client = await pool.connect()

        let account = await client.query(`SELECT *
                                          FROM ACCOUNT
                                          WHERE user_name = '${userName}'`);
        const result = Promise.resolve({
            userName: account.rows[0].user_name,
            password: account.rows[0].password,
            firstName: account.rows[0].first_name,
            lastName: account.rows[0].last_name
        })

        client.release()
        return result
    }

    async save(user: User): Promise<void> {
        const client = await pool.connect()

        await client.query(`INSERT INTO ACCOUNT (USER_NAME, PASSWORD, FIRST_NAME, LAST_NAME)
                            VALUES ('${user.userName}', '${user.password}', '${user.firstName}',
                                    '${user.lastName}')`);
        client.release()
        return Promise.resolve()
    }

}


export function registerUserEndPointFor(app: Express) {
    const userRepository: UserRepository = new PostGressUserRepository()

    app.post('/account', (req: Request, res: Response) => {
        const user = req.body as User;
        userRepository.save(user)
            .then((_) => res.status(201).end())
    });
}
