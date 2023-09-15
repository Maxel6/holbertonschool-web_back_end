export default class Currency {
  constructor(code, name) {
    if (typeof code !== 'string') {
      throw new Error('Code should be a string');
    }
    if (typeof name !== 'string') {
      throw new Error('Name should be a string');
    }
    this._code = code;
    this._name = name;
  }

  get code() {
    return this._code;
  }

  set code(code) {
    if (typeof code !== 'string') {
      throw new Error('Code should be a string');
    }
    this._code = code;
  }

  get name() {
    return this._name;
  }

  set name(name) {
    if (typeof name !== 'string') {
      throw new Error('Name should be a string');
    }
    this._name = name;
  }

  displayFullCurrency() {
    return `${this.name} (${this.code})`;
  }
}
