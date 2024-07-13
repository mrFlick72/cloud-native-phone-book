import {User} from "./user";
import {SignJWT} from "jose";
import {JWK_KID, jwtSignaturePrivateKey} from "./jwk";

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
            "user_name": `${user.userName}`,
            "first_name": `${user.firstName}`,
            "last_name": `${user.lastName}`
        };
        const token = await new SignJWT(payload) // details to  encode in the token
            .setProtectedHeader({
                kid: JWK_KID,
                typ: "JWT",
                alg: 'RS256'
            }) // algorithm
            .setIssuedAt()
            .setIssuer(process.env.JWT_ISSUER || "http://localhost:3000") // issuer
            .setAudience(process.env.JWT_AUDIENCE || "http://localhost:5000") // audience
            .setExpirationTime(process.env.JWT_EXPIRATION_TIME || "1h") // token expiration time, e.g., "1 day"
            .sign(jwtSignaturePrivateKey);

        return Promise.resolve({content: token})
    }
}
