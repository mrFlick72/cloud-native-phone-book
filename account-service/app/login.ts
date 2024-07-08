import {Express, Request, Response} from 'express';
import {loginTokenService, LoginTokenService, Token} from "./token";
import {User, UserRepository, userRepository} from "./user";

export type UserNameAndPassword = {
    userName: string
    password: string
}

export class UserLoginService {

    private userRepository: UserRepository
    private loginTokenService: LoginTokenService

    constructor(
        userRepository: UserRepository,
        loginTokenService: LoginTokenService
    ) {
        this.userRepository = userRepository
        this.loginTokenService = loginTokenService
    }

    async loginFor(userName: string, password: string): Promise<Token> {
        const user: User = await this.userRepository.findUserBy(userName)
        if (user.password === password) {
            const loginToken: Token = await this.loginTokenService.getLoginTokenFor(user)
            return Promise.resolve(loginToken)
        } else {
            return Promise.reject()
        }

    }
}

export function registerLoginEndPointFor(app: Express) {
    const userLoginService: UserLoginService = new UserLoginService(
        userRepository(),
        loginTokenService()
    )

    app.post('/login', async (req: Request, res: Response) => {
        const userNameAndPassword = req.body as UserNameAndPassword;
        const loginToken = await userLoginService.loginFor(userNameAndPassword.userName, userNameAndPassword.password)
        res.send(loginToken)
    });
}
