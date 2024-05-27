#!/usr/bin/node

import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default function handleProfileSignup(firstName, lastName, fileName) {
  const userPromise = signUpUser(firstName, lastName).then(value => ({
    status: 'fulfilled',
    value,
  })).catch(error => ({
    status: 'rejected',
    value: error.toString(),
  }));

  const photoPromise = uploadPhoto(fileName).then(value => ({
    status: 'fulfilled',
    value,
  })).catch(error => ({
    status: 'rejected',
    value: error.toString(),
  }));

  return Promise.allSettled([userPromise, photoPromise]);
}
