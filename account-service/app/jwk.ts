import {createPrivateKey, createPublicKey, createSecretKey, generateKeyPairSync} from "node:crypto";
import {Express, Request, Response} from "express";
import {exportJWK} from "jose";


// KeyObject  is a representation of a key/ secret available in the Node.
// js runtime.
// In addition to the import functions of this library you may use the runtime APIs crypto.
// createPublicKey , crypto. createPrivateKey , and crypto. createSecretKey  to obtain a KeyObject from your existing key material.
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
