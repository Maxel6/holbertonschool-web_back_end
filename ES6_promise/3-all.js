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
    .catch(() => {
      console.log('Signup system offline');
      return new Error();
    });
}
