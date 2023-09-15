export default class Building {
  constructor(sqft) {
    if (typeof sqft !== 'number') {
      throw new Error('Square footage should be a number');
    }
    this._sqft = sqft;
  }

  get sqft() {
    return this._sqft;
  }

  static evacuationWarningMessage() {
    throw new Error('Class extending Building must override evacuationWarningMessage');
  }
}
