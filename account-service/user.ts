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
    return new FixedUerRepository()
}

class FixedUerRepository implements UserRepository {
    findUserBy(userName: string): Promise<User> {
        return Promise.resolve({
            userName: "vvaudi",
            password: "secret",
            firstName: "Valerio",
            lastName: "Vaudi"
        })
    }

    save(user: User): Promise<void> {
        throw new Error("Method not implemented.")
    }

}