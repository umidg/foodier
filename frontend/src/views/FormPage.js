/* eslint-disable */
import {
  Button,
  Group,
  Select,
  Stepper,
  TextInput,
  MultiSelect,
} from '@mantine/core';
import React, { useEffect, useState } from 'react';
import { useForm } from '@mantine/form';
import { Table } from '@mantine/core';
import { api } from '../api';

export default function Formpage({ setState }) {
  const colorPallete = [
    '#C1ECE4',
    '#FFD6A5',
    '#FFFEC4',
    '#CBFFA9',
    '#E6FFFD',
    '#D0F5BE',
    '#FBFFDC',
  ];
  const [response, setResponse] = useState(null);
  //setting active step for stepper
  const [active, setActive] = useState(0);
  const nextStep = () =>
    setActive((current) => (current < 3 ? current + 1 : current));
  const prevStep = () =>
    setActive((current) => (current > 0 ? current - 1 : current));

  // mantine form hook
  const form = useForm({
    initialValues: {
      daysofweek: 'whole week',
      name: '',
      weight: null,
      height: null,
      age: null,
      diet: '',
      allergies: '',
      favfood: '',
      budget: null,
      meals: null,
    },
  });

  //after pressing submit function
  const nextStepSubmit = async () => {
    console.log(form.values);
    api('/api', { ...form.values }, 'POST')
      .then((data) => {
        if (data.data.message) setResponse(JSON.parse(data.data.message));
      })
      .catch((e) => console.log(e));
    nextStep();
  };

  useEffect(() => {}, response);

  const rows = (e, i) => {
    const data = response[e];
    return (
      <tr
        key={data.Breakfast}
        style={{
          margin: '10px auto',
          backgroundColor: colorPallete[i],
        }}
      >
        <td
          style={{
            // backgroundColor: 'red',
            padding: '20px 10px',
            fontWeight: 'bolder',
            fontSize: '20px',
            borderRight: '3px solid #cccccc',
          }}
        >
          {e}
        </td>
        <td>{data.Breakfast || '-'}</td>
        <td>{data.Lunch || '-'}</td>
        <td>{data.Dinner || '-'}</td>
      </tr>
    );
  };

  // Three steps with labels
  return (
    <div>
      <form>
        <Stepper active={active} onStepClick={setActive} breakpoint='sm'>
          <Stepper.Step label='User Information'>
            <TextInput
              label='Name'
              placeholder='Enter your name'
              {...form.getInputProps('name')}
            />
            <br />
            <TextInput
              label='Weight (in Kg)'
              type='number'
              placeholder='Enter your weight'
              {...form.getInputProps('weight')}
            />
            <br />
            <TextInput
              label='Height (in cm)'
              type='number'
              placeholder='Enter your height'
              {...form.getInputProps('height')}
            />
            <br />
            <Select
              label='Gender'
              placeholder='Select your gender'
              data={[
                { value: 'male', label: 'Male' },
                { value: 'female', label: 'Female' },
                { value: 'non-binary', label: 'Non-binary' },
                { value: 'none', label: 'Prefer not to say' },
              ]}
              {...form.getInputProps('gender')}
            />
            <br />
            <TextInput
              label='Age'
              type='number'
              placeholder='Enter your age'
              {...form.getInputProps('age')}
            />
            <br />
          </Stepper.Step>
          <Stepper.Step label='Food Preferences'>
            <TextInput
              label='Diet (e.g. vegan, vegetrian, non-vegeterian...)'
              placeholder='Enter your diet (use comma for more than one)'
              {...form.getInputProps('diet')}
            />
            <br />
            <TextInput
              label='Allergies (e.g. peanut, gluten...)'
              placeholder='Enter your allegies (use comma for more than one)'
              {...form.getInputProps('allergies')}
            />
            <br />
            <TextInput
              label='Favorite Food (e.g. sushi, porridge, haka noodles...)'
              placeholder='Enter your fav food (use comma for more than one)'
              {...form.getInputProps('favfood')}
            />
          </Stepper.Step>
          <Stepper.Step label='Meal Choices'>
            <TextInput
              label='Budget'
              placeholder='Enter your budget in CAD'
              type='number'
              {...form.getInputProps('budget')}
            />
            <br />
            <Select
              label='Days of Week'
              data={[
                { value: 'weekdays', label: 'Weekdays' },
                { value: 'weekends', label: 'Weekends' },
                { value: 'whole week', label: 'Whole Week' },
              ]}
              {...form.getInputProps('daysofweek')}
            />
            <br />
            <MultiSelect
              data={[
                { value: 'breakfast', label: 'Breakfast' },
                { value: 'lunch', label: 'Lunch' },
                { value: 'dinner', label: 'Dinner' },
              ]}
              label='Meals a day'
              placeholder='Select multiple meals'
              {...form.getInputProps('meals')}
            />
          </Stepper.Step>

          <Stepper.Completed>
            {response ? (
              <>
                <Table>
                  <thead>
                    <tr
                      style={{
                        border: '3px solid #eeeeee',
                        fontSize: '20px',
                      }}
                    >
                      <th
                        style={{
                          fontSize: '20px',
                          borderRight: '3px solid #cccccc',
                        }}
                      >
                        Day
                      </th>
                      <th
                        style={{
                          padding: '20px',
                          fontSize: '20px',
                        }}
                      >
                        Breakfast
                      </th>
                      <th
                        style={{
                          fontSize: '20px',
                        }}
                      >
                        Lunch
                      </th>
                      <th
                        style={{
                          fontSize: '20px',
                        }}
                      >
                        Dinner
                      </th>
                    </tr>
                  </thead>
                  <tbody>
                    {Object.keys(response).map((e, i) => {
                      if (e !== 'Ingredients') return rows(e, i);
                    })}
                  </tbody>
                </Table>
                <br />
                <div>
                  <p
                    style={{
                      fontWeight: 'bolder',
                    }}
                  >
                    Ingridients:
                  </p>

                  {response.Ingredients.map((eachIngridient, index) => {
                    return (
                      eachIngridient.charAt(0).toUpperCase() +
                      eachIngridient.slice(1) +
                      ', '
                    );
                  })}
                </div>
              </>
            ) : (
              <p>Loading...</p>
            )}
          </Stepper.Completed>
        </Stepper>

        <Group position='center' mt='xl'>
          {active !== 0 && active < 3 && (
            <Button variant='default' onClick={prevStep}>
              Back
            </Button>
          )}
          {active < 2 ? (
            <Button onClick={nextStep}>Next step</Button>
          ) : active === 2 ? (
            <Button onClick={nextStepSubmit}>Submit</Button>
          ) : (
            <></>
          )}
        </Group>
      </form>
    </div>
  );
}
