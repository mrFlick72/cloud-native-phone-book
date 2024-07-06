import {User} from "./user";

export type Token = {
    content: string
}

export interface LoginTokenService {
    getLoginTokenFor(user: User): Promise<Token>
}

export function loginTokenService() {
    return new JwtLoginTokenService()
}

class JwtLoginTokenService implements LoginTokenService {

    getLoginTokenFor(user: User): Promise<Token> {
        return Promise.resolve({content: "JWT"})
    }
}
