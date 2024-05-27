export default function updateStudentGradeByCity(students, city, newGrades) {
  return students
    .filter((student) => student.location === city)
    .map((student) => {
      const studentGradeObj = newGrades
        .find((newStudent) => newStudent.studentId === student.id);

      return {
        ...student,
        grade: studentGradeObj && studentGradeObj.grade
          ? studentGradeObj.grade : 'N/A',
      };
    });
}
