export default class Airport {
  constructor(name, code) {
    if (typeof name !== 'string') {
      throw new Error('Name should be a string');
    }
    if (typeof code !== 'string') {
      throw new Error('Code should be a string');
    }
    this._name = name;
    this._code = code;
  }

  get [Symbol.toStringTag]() {
    return this._code;
  }
}
