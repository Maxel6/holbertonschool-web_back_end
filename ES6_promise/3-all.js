import { uploadPhoto, createUser } from './utils.js';

export default function handleProfileSignup() {
  return Promise.all([uploadPhoto(), createUser()])
    .then(([photoResult, userResult]) => {
      const photo = photoResult.body;
      const user = `${userResult.firstName} ${userResult.lastName}`;

      console.log(photo, user);

      return {
        status: 200,
        body: `${photo} ${user}`,
      };
    })
    .catch((error) => {
      console.error('Signup system offline', error);

      return {
        status: 500,
        body: 'Signup system offline',
      };
    });
}
