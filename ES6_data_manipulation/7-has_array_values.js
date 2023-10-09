export default function hasValuesFromArray(set, array) {
  const areAllElementsInSet = array.every((element) => set.has(element));
  return areAllElementsInSet;
}
