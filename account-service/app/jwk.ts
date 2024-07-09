import {createPrivateKey, createPublicKey, createSecretKey, generateKeyPairSync} from "node:crypto";
import {Express, Request, Response} from "express";
import {exportJWK} from "jose";

const {
    publicKey,
    privateKey,
} = generateKeyPairSync('rsa', {
    modulusLength: 4096,
    publicKeyEncoding: {
        type: 'spki',
        format: 'pem'
    },
    privateKeyEncoding: {
        type: 'pkcs8',
        format: 'pem'
    }
});

export const jwtSignaturePublicKey = createPublicKey(publicKey);
export const jwtSignaturePrivateKey = createPrivateKey(privateKey);

export async function registerJwkEndpointFor(app: Express) {

    const jwk = await exportJWK(jwtSignaturePublicKey);

    app.get('/jwks', (req: Request, res: Response) => {
        res.send(jwk)
    });
}
