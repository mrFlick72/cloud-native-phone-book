import {User} from "./user";
import {SignJWT} from "jose";
import {jwtSignatureSecretKey} from "./jwk";

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

    async getLoginTokenFor(user: User): Promise<Token> {
        let payload = {
            "user-name": `${user.userName}`,
            "first-name": `${user.firstName}`,
            "last-name": `${user.lastName}`
        };
        const token = await new SignJWT(payload) // details to  encode in the token
            .setProtectedHeader({
                typ: "JWT",
                alg: 'RS256'
            }) // algorithm
            .setIssuedAt()
            .setIssuer(process.env.JWT_ISSUER || "http://localhost") // issuer
            .setAudience(process.env.JWT_AUDIENCE || "http://localhost") // audience
            .setExpirationTime(process.env.JWT_EXPIRATION_TIME || "1h") // token expiration time, e.g., "1 day"
            .sign(jwtSignatureSecretKey);

        return Promise.resolve({content: token})
    }
}
