export default function getStudentIdsSum(studentsList) {
  const totalIdSum = studentsList.reduce((sum, student) => sum + student.id, 0);
  return totalIdSum;
}
