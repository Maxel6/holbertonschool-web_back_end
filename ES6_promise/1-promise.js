export default function getFullResponseFromAPI(success) {
  return new Promise((resolve, reject) => {
    if (succes) {
      const reponse = {
        status: 200,
        body: 'Succes',
      };
      resolve(reponse);
    } else {
      const error = new Error('The fake API is not working currently');
      reject(error);
    }
  });
}
