import { uploadPhoto, createUser } from './utils';

export default function handleProfileSignup() {
  let photo;
  let user;

  return Promise.all([uploadPhoto(), createUser()])
    .then(([photoResult, userResult]) => {
      photo = photoResult.body;
      user = `${userResult.firstName} ${userResult.lastName}`;

      const resultString = `${photo} ${user}`;
      console.log(resultString);

      return {
        status: 200,
        body: resultString,
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
