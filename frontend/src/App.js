/* eslint-disable */
import { useEffect, useState } from 'react';
import { Center, Container, createStyles, Header } from '@mantine/core';
import Formpage from './views/FormPage';

//creating classes using createstyles from mantine
const useStyles = createStyles((theme) => ({
  header: {
    backgroundColor: '#5765F2',
  },
  titleText: {
    color: 'white',
    fontSize: '32px',
    fontWeight: 'bolder',
    alignItems: 'center',
  },
  wrapper: {
    paddingTop: `calc(${theme.spacing.xl} * 2)`,
    minHeight: '100vh',
    width: '100%',
    backgroundColor: `#5765F200`,
    position: 'relative',
    color: theme.black,
  },
  mainContainer: {
    backgroundColor: 'white',
    padding: '2%',
    borderRadius: '5px 5px',
    boxShadow: '0px 0px 5px #dddddd',
  },
}));

function App() {
  //main state to save form
  const [mainState, setMainState] = useState({});
  const { classes } = useStyles();

  //useeffect
  useEffect(() => {
    console.log(mainState);
  }, mainState);

  return (
    <div>
      <Header height={56} className={classes.header}>
        <Center className={classes.titleText}>Foodier</Center>
      </Header>
      <div className={classes.wrapper}>
        <Container size='sm' className={classes.mainContainer}>
          {/* passing setmainstate function to child component */}
          <Formpage setState={setMainState} />
        </Container>
      </div>
    </div>
  );
}

export default App;
