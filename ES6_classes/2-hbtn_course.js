export default class HolbertonCourse {
  constructor(name, length, students) {
    if (typeof name !== 'string') {
      throw new Error('Name should be a string');
    }
    if (typeof length !== 'number') {
      throw new Error('Length should be a number');
    }
    if (!Array.isArray(students) || students.some((student) => typeof student !== 'string')) {
      throw new Error('Students should be an array of strings');
    }

    this._name = name;
    this._length = length;
    this._students = students;
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

  get length() {
    return this._length;
  }

  set length(length) {
    if (typeof length !== 'number') {
      throw new Error('Length should be a number');
    }
    this._length = length;
  }

  get students() {
    return this._students;
  }

  set students(students) {
    if (!Array.isArray(students) || students.some((student) => typeof student !== 'string')) {
      throw new Error('Students should be an array of strings');
    }
    this._students = students;
  }
}
