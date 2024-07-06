import {User} from "./user";
import {SignJWT, UnsecuredJWT} from "jose";
import {createSecretKey} from "node:crypto";

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
    private secretKey = createSecretKey(process.env.JWT_SECRET || "1234567890987654321", 'utf-8');

    async getLoginTokenFor(user: User): Promise<Token> {
        let payload = {
            "user-name": `${user.userName}`,
            "first-name": `${user.firstName}`,
            "last-name": `${user.lastName}`
        };
        const token = await new SignJWT(payload) // details to  encode in the token
            .setProtectedHeader({
                alg: 'HS256'
            }) // algorithm
            .setIssuedAt()
            .setIssuer(process.env.JWT_ISSUER || "http://localhost") // issuer
            .setAudience(process.env.JWT_AUDIENCE || "http://localhost") // audience
            .setExpirationTime(process.env.JWT_EXPIRATION_TIME || "1h") // token expiration time, e.g., "1 day"
            .sign(this.secretKey);
        const unsecuredJwt = new UnsecuredJWT(payload)
            .setIssuedAt()
            .setIssuer('http://localhost:3000')
            .setAudience('http://localhost:5000')
            .setExpirationTime('2h')
            .encode()
        return Promise.resolve({content: token})
    }
}
