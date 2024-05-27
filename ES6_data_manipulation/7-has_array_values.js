export default function hasValuesFromArray(set, array) {
	//  Testing hotfix
  return array.every(value => set.has(value));
}
