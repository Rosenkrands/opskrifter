import { Typography, Stack, Paper, Box } from '@mui/material';
import RestaurantIcon from '@mui/icons-material/Restaurant';

export default function Home() {
    return (
        <Box>
            <Stack spacing={1}>
                <Paper elevation={5} sx={{ backgroundColor: "tomato", color: "yellow" }}>
                    <Box padding="10px">
                        <Stack direction="row" alignItems="center" justifyContent={"space-between"}>
                            <Typography variant="h2">Madplanlægger</Typography>
                            <RestaurantIcon fontSize="large" />
                        </Stack>
                    </Box>
                </Paper>
                <Paper elevation={5}>
                    <Box padding="10px">
                        <Stack direction="row" alignItems="center" justifyContent={"space-evenly"}>
                            <Typography variant="button">Opskrifter</Typography>
                            <Typography variant="button">Indkøbsliste</Typography>
                            <Typography variant="button">Ingredienser</Typography>
                            <Typography variant="button">Enheder</Typography>
                        </Stack>
                    </Box>
                </Paper>
                <Paper elevation={5}>
                    <Box padding={"10px"}>
                        <Typography variant="body2">Præsentation af "Madplanlægger"

                            Velkommen til Madplanlægger - din personlige assistent til nem og bekvem madlavning!

                            Formål:
                            Madplanlægger er din ultimative løsning til at organisere dine madlavningsoplevelser og forenkle dine indkøb ved at tilbyde en samlet indkøbsliste baseret på de valgte opskrifter.

                            Funktioner:

                            Opskriftsdatabase: Vores omfattende database indeholder et væld af opskrifter, fra traditionelle favoritter til innovative retter. Søg efter opskrifter baseret på forskellige kriterier som køkken, type, sværhedsgrad og ingredienser.

                            Opskriftsvalg og Tilpasning: Vælg dine yndlingsopskrifter fra vores database og tilføj dem til din personlige madplan. Tilpas portioner for at matche dine behov.

                            Samlet Indkøbsliste: Efter at have valgt dine opskrifter, genererer Madplanlægger automatisk en samlet indkøbsliste med alle nødvendige ingredienser. Dette gør dine indkøbsture mere effektive og reducerer spild.

                            Indkøbsliste Management: Rediger din indkøbsliste efter behov ved at tilføje eller fjerne elementer og markere allerede købte varer. Gem dine indkøbslister til senere brug.

                            Fællesskabsfunktioner: Del dine yndlingsopskrifter med andre brugere og opdag nye retter fra fællesskabets bidragydere. Kommenter og bedøm opskrifter for at hjælpe andre brugere med deres madlavningsoplevelser.

                            Hvordan det fungerer:

                            Registrering: Opret en konto på Madplanlægger for at få adgang til alle funktionerne.

                            Søg og Vælg: Gennemse vores opskriftsdatabase, vælg dine favoritopskrifter, og tilføj dem til din madplan.

                            Generer Indkøbsliste: Når du er klar til at handle, genererer Madplanlægger automatisk en samlet indkøbsliste baseret på dine valgte opskrifter.

                            Handle og Nyd: Tag din indkøbsliste med dig til butikken, køb ingredienserne, og nyd en problemfri madlavningsoplevelse derhjemme!

                            Madplanlægger - din partner i madlavningens verden, hvor planlægning bliver nem, og resultatet er velsmagende!</Typography>
                    </Box>
                </Paper>
            </Stack>
        </Box>
    )
} 