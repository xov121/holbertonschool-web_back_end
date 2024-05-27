export default function hasValuesFromArray(set, array) {
  // for every item in ``array``: check that it's present in ``set``.
  // If even one item in ``array`` isn't present in set, return false.
  return array.every((item) => set.has(item));
}
