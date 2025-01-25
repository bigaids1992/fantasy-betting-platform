import React, { useState, useEffect } from "react";
import { Card, CardContent } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Table, TableHeader, TableRow, TableHead, TableBody, TableCell } from "@/components/ui/table";
import { MotionDiv } from "framer-motion";
import Image from "next/image";
import * as XLSX from 'xlsx';

const FantasySportsbook = () => {
  const [betSlip, setBetSlip] = useState([]);
  const [fantasyTeams, setFantasyTeams] = useState([]);

  useEffect(() => {
    // Load the predefined fantasy matchup file
    fetch("/mnt/data/fantasy_matchup_upload.xlsx")
      .then(response => response.arrayBuffer())
      .then(buffer => {
        const workbook = XLSX.read(buffer, { type: "array" });
        const sheetName = workbook.SheetNames[0];
        const sheet = XLSX.utils.sheet_to_json(workbook.Sheets[sheetName], { header: 1 });
        
        const teams = [];
        for (let i = 1; i < sheet.length; i++) {
          const [position, team1Player, team1Odds, team2Player, team2Odds] = sheet[i];
          if (team1Player && team2Player) {
            teams.push(
              { id: i, name: "The Gridion Grandpas", player: team1Player, odds: team1Odds, img: "/mnt/data/4329ABF7-94BF-4073-8CA8-7ED37302BD69.png" },
              { id: i + 100, name: "Graveskowski Marches on", player: team2Player, odds: team2Odds, img: "/mnt/data/CF878958-A74B-4CCE-881B-6F66B4005940.webp" }
            );
          }
        }
        setFantasyTeams(teams);
      });
  }, []);

  const addToBetSlip = (team) => {
    setBetSlip([...betSlip, team]);
  };

  const calculateOdds = () => {
    return betSlip.reduce((acc, team) => acc * team.odds, 1).toFixed(2);
  };

  return (
    <div className="p-6 bg-cover bg-center" style={{ backgroundImage: 'url(/mnt/data/A_sleek,_modern_sportsbook_background_for_Fantasy_.png)' }}>
      <div className="flex justify-center mb-6">
        <Image src="/mnt/data/IMG_9766-remove-background.com.png" alt="Fantasy Champions Logo" width={300} height={100} />
      </div>
      <h1 className="text-2xl font-bold mb-4 text-white">Fantasy Champions Sportsbook</h1>
      <Table>
        <TableHeader>
          <TableRow>
            <TableHead>Team</TableHead>
            <TableHead>Player</TableHead>
            <TableHead>Odds</TableHead>
            <TableHead>Action</TableHead>
          </TableRow>
        </TableHeader>
        <TableBody>
          {fantasyTeams.map((team) => (
            <TableRow key={team.id}>
              <TableCell>
                <div className="flex items-center space-x-2">
                  <Image src={team.img} alt={team.name} width={50} height={50} className="rounded-full" />
                  <span>{team.name}</span>
                </div>
              </TableCell>
              <TableCell>{team.player}</TableCell>
              <TableCell>{team.odds}</TableCell>
              <TableCell>
                <Button onClick={() => addToBetSlip(team)}>Add to BetSlip</Button>
              </TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
      
      <Card className="mt-6 bg-gray-900 text-white">
        <CardContent>
          <h2 className="text-xl font-semibold">Bet Slip</h2>
          {betSlip.length > 0 ? (
            <ul>
              {betSlip.map((bet, index) => (
                <li key={index}>{bet.name} - {bet.odds}</li>
              ))}
            </ul>
          ) : (
            <p>No bets placed yet.</p>
          )}
          <p className="mt-4 font-semibold">Total Odds: {calculateOdds()}</p>
        </CardContent>
      </Card>
    </div>
  );
};

export default FantasySportsbook;
