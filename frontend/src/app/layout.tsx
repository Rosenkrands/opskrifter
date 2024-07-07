import { Box, Button, Paper, Stack, Typography } from "@mui/material"
import Link from "next/link"

export const metadata = {
  title: 'Madplanlægger',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="da">
      <body>
        <main>
          <Box padding={"10px"}>
            <Box paddingBottom={"10px"}>
              <Paper elevation={5}>
                <Box padding="10px">
                  <Stack direction="row" alignItems="center" justifyContent={"space-between"}>
                    <Typography variant="h2">Madplanlægger</Typography>
                  </Stack>
                  <Paper elevation={5}>
                    <Box padding="10px">
                      <Stack direction="row" alignItems="center" justifyContent={"space-evenly"}>
                        <Link href="/">Hjem</Link>
                        <Link href="/recipes">Opskrifter</Link>
                        <Link href="/grocieries">Indkøbsliste</Link>
                        <Link href="/indgredients">Ingredienser</Link>
                        <Link href="/uits">Enheder</Link>
                      </Stack>
                    </Box>
                  </Paper>
                </Box>
              </Paper>
            </Box>
            {children}
          </Box>
        </main>
      </body>
    </html>
  )
}
