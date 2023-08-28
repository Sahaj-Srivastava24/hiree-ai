interface User {
  username: string;
  email: string;
  password: string;
}

const userDatabase: User[] = [
  {
    username: 'admin123',
    email: 'admin123@example.com',
    password: 'password123',
  },
  {
    username: 'john_doe',
    email: 'john.doe@example.com',
    password: 'doe456',
  },
  {
    username: 'jane_smith',
    email: 'jane.smith@example.com',
    password: 'smith789',
  },
]; // This will simulate your user database

export function signUp(newUser: User): Promise<void> {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      userDatabase.push(newUser);
      resolve();
    }, 1000); // Simulating a 1 second network delay
  });
}

export function login(email: string, password: string): Promise<boolean> {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      const user = userDatabase.find(
        (user) => user.email === email && user.password === password
      );
      resolve(user !== undefined);
    }, 1500); // Simulating a 1.5 second network delay
  });
}
